from flask import Blueprint, request, jsonify
from ..models import User, Lecture, Enrollment, db

timetable_bp = Blueprint('timetable', __name__)

@timetable_bp.route('/timetables', methods=['GET'])
def get_timetable():
    # 1. 사용자 인증 (임시) - 학번을 쿼리 파라미터로 직접 받음
    student_id = request.args.get('student_id')
    if not student_id:
        return jsonify({'error': '학번(student_id) 정보가 필요합니다'}), 400

    user = User.query.filter_by(student_id=student_id).first()
    if not user:
        return jsonify({'error': '사용자를 찾을 수 없습니다'}), 404

    # 2. 학기 정보 받아오기
    semester = request.args.get('semester')
    if not semester:
        return jsonify({'error': '학기(semester) 정보가 필요합니다'}), 400

    # 3. 데이터베이스 쿼리
    timetable_lectures = db.session.query(Lecture).join(Enrollment).filter(
        Enrollment.user_id == user.id,
        Lecture.semester == semester
    ).all()

    # 4. 결과 JSON으로 변환
    result = [
        {
            "lecture_id": lecture.lecture_id,
            "subject": lecture.subject,
            "professor": lecture.professor,
            "weekday": lecture.weekday,
            "start_time": lecture.start_time,
            "end_time": lecture.end_time,
            "room": lecture.room
        }
        for lecture in timetable_lectures
    ]

    return jsonify(result), 200
