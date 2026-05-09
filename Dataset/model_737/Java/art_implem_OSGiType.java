





import java.util.List;
import java.util.ArrayList;

public class art_implem_OSGiType extends TypeImplementation {

    private String generateInstanceBundle;



    public art_implem_OSGiType(
        String generateInstanceBundle    ) {
        super(
        );
        this.generateInstanceBundle = generateInstanceBundle;
    }


    public String getGenerateinstancebundle() {
        return generateInstanceBundle;
    }

    public void setGenerateinstancebundle(String generateInstanceBundle) {
        this.generateInstanceBundle = generateInstanceBundle;
    }


}