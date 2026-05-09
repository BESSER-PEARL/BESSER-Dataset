





import java.util.List;
import java.util.ArrayList;

public class DOM_Name extends Expression {

    private String fullyQualifiedName;



    public DOM_Name(
        String fullyQualifiedName    ) {
        super(
        );
        this.fullyQualifiedName = fullyQualifiedName;
    }


    public String getFullyqualifiedname() {
        return fullyQualifiedName;
    }

    public void setFullyqualifiedname(String fullyQualifiedName) {
        this.fullyQualifiedName = fullyQualifiedName;
    }


}