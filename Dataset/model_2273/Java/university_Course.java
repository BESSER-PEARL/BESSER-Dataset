





import java.util.List;
import java.util.ArrayList;

public class university_Course  {

    private String name;
    private int etcs;
    private String id;





    private university_CourseCatalog university_coursecatalog;


    public university_Course(
        String name,        int etcs,        String id    ) {
        this.name = name;
        this.etcs = etcs;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getEtcs() {
        return etcs;
    }

    public void setEtcs(int etcs) {
        this.etcs = etcs;
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