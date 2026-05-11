





import java.util.List;
import java.util.ArrayList;

public class universityextended_people_Professor extends Person {

    private String rank;





    private List<Lecture> lectures;


    public universityextended_people_Professor(
        String rank    ) {
        super(
        );
        this.rank = rank;
        this.lectures = new ArrayList<>();
    }

    public universityextended_people_Professor(
        String rank        ArrayList<Lecture> lectures    ) {
        this.rank = rank;
        this.lectures = lectures;
    }

    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }

    public List<Lecture> getLectures() {
        return lectures;
    }

    public void addLecture(Lecture lecture) {
        this.lectures.add(lecture);
    }

}