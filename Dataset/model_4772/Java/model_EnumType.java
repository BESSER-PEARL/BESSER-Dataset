





import java.util.List;
import java.util.ArrayList;

public class model_EnumType extends Type {

    private String name;
    private String literals;



    public model_EnumType(
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