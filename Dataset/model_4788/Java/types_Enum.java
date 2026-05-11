





import java.util.List;
import java.util.ArrayList;

public class types_Enum extends Simple {

    private String literals;
    private String name;



    public types_Enum(
        String literals,        String name    ) {
        super(
        );
        this.literals = literals;
        this.name = name;
    }


    public String getLiterals() {
        return literals;
    }

    public void setLiterals(String literals) {
        this.literals = literals;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}