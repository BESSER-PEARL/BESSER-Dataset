





import java.util.List;
import java.util.ArrayList;

public class university_Course  {

    private int etcs;
    private String name;
    private String id;





    private university_CourseCatalog university_coursecatalog;


    public university_Course(
        int etcs,        String name,        String id    ) {
        this.etcs = etcs;
        this.name = name;
        this.id = id;
    }


    public int getEtcs() {
        return etcs;
    }

    public void setEtcs(int etcs) {
        this.etcs = etcs;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public university_CourseCatalog getUniversity_coursecatalog() {
        return university_coursecatalog;
    }

    public void setUniversity_coursecatalog(university_CourseCatalog university_coursecatalog) {
        this.university_coursecatalog = university_coursecatalog;
    }

}