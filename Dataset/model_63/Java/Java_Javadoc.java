





import java.util.List;
import java.util.ArrayList;

public class Java_Javadoc extends Comment {






    private List<Java_TagElement> java_tagelements;


    public Java_Javadoc(
    ) {
        super(
        );
        this.java_tagelements = new ArrayList<>();
    }

    public Java_Javadoc(
        ArrayList<Java_TagElement> java_tagelements    ) {
        this.java_tagelements = java_tagelements;
    }


    public List<Java_TagElement> getJava_tagelements() {
        return java_tagelements;
    }

    public void addJava_tagelement(Java_tagelement java_tagelement) {
        this.java_tagelements.add(java_tagelement);
    }

}