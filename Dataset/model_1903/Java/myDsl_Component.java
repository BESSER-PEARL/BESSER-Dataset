





import java.util.List;
import java.util.ArrayList;

public class myDsl_Component  {

    private String name;





    private myDsl_Architecture mydsl_architecture;


    public myDsl_Component(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Architecture getMydsl_architecture() {
        return mydsl_architecture;
    }

    public void setMydsl_architecture(myDsl_Architecture mydsl_architecture) {
        this.mydsl_architecture = mydsl_architecture;
    }

}