





import java.util.List;
import java.util.ArrayList;

public class java_Javadoc extends Comment {






    private List<java_TagElement> java_tagelements;


    public java_Javadoc(
    ) {
        super(
        );
        this.java_tagelements = new ArrayList<>();
    }

    public java_Javadoc(
        ArrayList<java_TagElement> java_tagelements    ) {
        this.java_tagelements = java_tagelements;
    }


    public List<java_TagElement> getJava_tagelements() {
        return java_tagelements;
    }

    public void addJava_tagelement(Java_tagelement java_tagelement) {
        this.java_tagelements.add(java_tagelement);
    }

}