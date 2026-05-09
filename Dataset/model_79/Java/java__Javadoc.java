





import java.util.List;
import java.util.ArrayList;

public class java__Javadoc extends Comment {






    private List<java__TagElement> java__tagelements;


    public java__Javadoc(
    ) {
        super(
        );
        this.java__tagelements = new ArrayList<>();
    }

    public java__Javadoc(
        ArrayList<java__TagElement> java__tagelements    ) {
        this.java__tagelements = java__tagelements;
    }


    public List<java__TagElement> getJava__tagelements() {
        return java__tagelements;
    }

    public void addJava__tagelement(Java__tagelement java__tagelement) {
        this.java__tagelements.add(java__tagelement);
    }

}