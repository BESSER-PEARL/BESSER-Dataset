





import java.util.List;
import java.util.ArrayList;

public class coursePages_CourseWork  {






    private List<coursePages_CourseWorkObject> coursepages_courseworkobjects;


    public coursePages_CourseWork(
    ) {
        this.coursepages_courseworkobjects = new ArrayList<>();
    }

    public coursePages_CourseWork(
        ArrayList<coursePages_CourseWorkObject> coursepages_courseworkobjects    ) {
        this.coursepages_courseworkobjects = coursepages_courseworkobjects;
    }


    public List<coursePages_CourseWorkObject> getCoursepages_courseworkobjects() {
        return coursepages_courseworkobjects;
    }

    public void addCoursepages_courseworkobject(Coursepages_courseworkobject coursepages_courseworkobject) {
        this.coursepages_courseworkobjects.add(coursepages_courseworkobject);
    }

}