from flask import Blueprint, request, jsonify

from ..models import User, Lecture, Attendance, db

from datetime import datetime


# 'attendance_bp' 라는 이름의 블루프린트 생성
attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/attendances', methods=['POST'])
def record_attendance():
    data = request.get_json()

    # 1. 요청 데이터 확인
    student_id = data.get('student_id')
    lecture_id = data.get('lecture_id') # 과목 코드로 받음
    status = data.get('status')

    if not all([student_id, lecture_id, status]):
        return jsonify({'error': 'student_id, lecture_id, status는 필수 항목입니다'}), 400

    # 2. 사용자와 강의 정보 조회
    user = User.query.filter_by(student_id=student_id).first()
    lecture = Lecture.query.filter_by(lecture_id=lecture_id).first()

    if not user or not lecture:
        return jsonify({'error': '사용자 또는 강의 정보를 찾을 수 없습니다'}), 404

    # 3. 출석 기록 생성 및 저장
    new_attendance = Attendance(
        user_id=user.id,
        lecture_id=lecture.id,
        status=status,
        recorded_at=datetime.utcnow() # 현재 시각(UTC)으로 기록
    )
    db.session.add(new_attendance)
    db.session.commit()

    # 4. 성공 응답 반환
    return jsonify({
        'message': '출석 기록이 성공적으로 저장되었습니다.',
        'attendance_id': new_attendance.id
    }), 201
