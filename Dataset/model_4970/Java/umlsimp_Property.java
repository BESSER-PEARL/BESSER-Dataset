





import java.util.List;
import java.util.ArrayList;

public class umlsimp_Property extends TypedElement {

    private String visibility;



    public umlsimp_Property(
        String visibility    ) {
        super(
        );
        this.visibility = visibility;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}