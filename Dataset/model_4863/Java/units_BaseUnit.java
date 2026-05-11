





import java.util.List;
import java.util.ArrayList;

public class units_BaseUnit extends Unit {

    private String name;



    public units_BaseUnit(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}