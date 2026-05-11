





import java.util.List;
import java.util.ArrayList;

public class types_Enum extends Simple {

    private String name;
    private String literals;



    public types_Enum(
        String name,        String literals    ) {
        super(
        );
        this.name = name;
        this.literals = literals;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLiterals() {
        return literals;
    }

    public void setLiterals(String literals) {
        this.literals = literals;
    }


}