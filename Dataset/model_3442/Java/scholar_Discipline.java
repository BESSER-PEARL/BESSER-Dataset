





import java.util.List;
import java.util.ArrayList;

public class scholar_Discipline extends Named {






    private scholar_Lecture scholar_lecture;


    public scholar_Discipline(
    ) {
        super(
        );
    }



    public scholar_Lecture getScholar_lecture() {
        return scholar_lecture;
    }

    public void setScholar_lecture(scholar_Lecture scholar_lecture) {
        this.scholar_lecture = scholar_lecture;
    }

}