





import java.util.List;
import java.util.ArrayList;

public class courceList_StudyProgram  {

    private int year;





    private courceList_StudyGeneralization courcelist_studygeneralization;




    private List<courceList_Student> courcelist_students;




    private courceList_StudyGeneralization courcelist_studygeneralization;




    private courceList_Student courcelist_student;


    public courceList_StudyProgram(
        int year    ) {
        this.year = year;
        this.courcelist_students = new ArrayList<>();
    }

    public courceList_StudyProgram(
        int year        ArrayList<courceList_Student> courcelist_students    ) {
        this.year = year;
        this.courcelist_students = courcelist_students;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public courceList_StudyGeneralization getCourcelist_studygeneralization() {
        return courcelist_studygeneralization;
    }

    public void setCourcelist_studygeneralization(courceList_StudyGeneralization courcelist_studygeneralization) {
        this.courcelist_studygeneralization = courcelist_studygeneralization;
    }
    public List<courceList_Student> getCourcelist_students() {
        return courcelist_students;
    }

    public void addCourcelist_student(Courcelist_student courcelist_student) {
        this.courcelist_students.add(courcelist_student);
    }
    public courceList_StudyGeneralization getCourcelist_studygeneralization() {
        return courcelist_studygeneralization;
    }

    public void setCourcelist_studygeneralization(courceList_StudyGeneralization courcelist_studygeneralization) {
        this.courcelist_studygeneralization = courcelist_studygeneralization;
    }
    public courceList_Student getCourcelist_student() {
        return courcelist_student;
    }

    public void setCourcelist_student(courceList_Student courcelist_student) {
        this.courcelist_student = courcelist_student;
    }

}