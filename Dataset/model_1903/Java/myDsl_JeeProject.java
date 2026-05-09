





import java.util.List;
import java.util.ArrayList;

public class myDsl_JeeProject  {

    private String name;





    private List<myDsl_Subproject> mydsl_subprojects;




    private myDsl_JavaApp mydsl_javaapp;


    public myDsl_JeeProject(
        String name    ) {
        this.name = name;
        this.mydsl_subprojects = new ArrayList<>();
    }

    public myDsl_JeeProject(
        String name        ArrayList<myDsl_Subproject> mydsl_subprojects    ) {
        this.name = name;
        this.mydsl_subprojects = mydsl_subprojects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<myDsl_Subproject> getMydsl_subprojects() {
        return mydsl_subprojects;
    }

    public void addMydsl_subproject(Mydsl_subproject mydsl_subproject) {
        this.mydsl_subprojects.add(mydsl_subproject);
    }
    public myDsl_JavaApp getMydsl_javaapp() {
        return mydsl_javaapp;
    }

    public void setMydsl_javaapp(myDsl_JavaApp mydsl_javaapp) {
        this.mydsl_javaapp = mydsl_javaapp;
    }

}