





import java.util.List;
import java.util.ArrayList;

public class simplepdl_RessourceDefinition extends ProcessElement {

    private String name;
    private int number;





    private simplepdl_RessourceInstance simplepdl_ressourceinstance;


    public simplepdl_RessourceDefinition(
        String name,        int number    ) {
        super(
        );
        this.name = name;
        this.number = number;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public simplepdl_RessourceInstance getSimplepdl_ressourceinstance() {
        return simplepdl_ressourceinstance;
    }

    public void setSimplepdl_ressourceinstance(simplepdl_RessourceInstance simplepdl_ressourceinstance) {
        this.simplepdl_ressourceinstance = simplepdl_ressourceinstance;
    }

}