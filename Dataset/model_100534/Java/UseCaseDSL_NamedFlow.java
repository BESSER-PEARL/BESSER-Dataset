





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_NamedFlow extends Flow {

    private String name;



    public UseCaseDSL_NamedFlow(
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