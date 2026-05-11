





import java.util.List;
import java.util.ArrayList;

public class panamaNeo4j_Entity  {

    private String name;





    private panamaNeo4j_Officer panamaneo4j_officer;


    public panamaNeo4j_Entity(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public panamaNeo4j_Officer getPanamaneo4j_officer() {
        return panamaneo4j_officer;
    }

    public void setPanamaneo4j_officer(panamaNeo4j_Officer panamaneo4j_officer) {
        this.panamaneo4j_officer = panamaneo4j_officer;
    }

}