





import java.util.List;
import java.util.ArrayList;

public class UseCaseDSL_LocalAlternative extends StepAlternative {

    private String description;



    public UseCaseDSL_LocalAlternative(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}