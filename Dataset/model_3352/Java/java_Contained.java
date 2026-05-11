





import java.util.List;
import java.util.ArrayList;

public class java_Contained  {

    private String visibility;





    private List<java_Class> java_classs;


    public java_Contained(
        String visibility    ) {
        this.visibility = visibility;
        this.java_classs = new ArrayList<>();
    }

    public java_Contained(
        String visibility        ArrayList<java_Class> java_classs    ) {
        this.visibility = visibility;
        this.java_classs = java_classs;
    }

    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public List<java_Class> getJava_classs() {
        return java_classs;
    }

    public void addJava_class(Java_class java_class) {
        this.java_classs.add(java_class);
    }

}