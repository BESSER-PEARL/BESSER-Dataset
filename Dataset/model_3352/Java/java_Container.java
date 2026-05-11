





import java.util.List;
import java.util.ArrayList;

public class java_Container  {






    private java_Contained java_contained;




    private List<java_Contained> java_containeds;


    public java_Container(
    ) {
        this.java_containeds = new ArrayList<>();
    }

    public java_Container(
        ArrayList<java_Contained> java_containeds    ) {
        this.java_containeds = java_containeds;
    }


    public java_Contained getJava_contained() {
        return java_contained;
    }

    public void setJava_contained(java_Contained java_contained) {
        this.java_contained = java_contained;
    }
    public List<java_Contained> getJava_containeds() {
        return java_containeds;
    }

    public void addJava_contained(Java_contained java_contained) {
        this.java_containeds.add(java_contained);
    }

}