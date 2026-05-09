





import java.util.List;
import java.util.ArrayList;

public class simplepdl_RessourceDefinition extends ProcessElement {

    private String name;
    private int number;



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


}