





import java.util.List;
import java.util.ArrayList;

public class rapidml_Extensible  {






    private List<rapidml_Extension> rapidml_extensions;


    public rapidml_Extensible(
    ) {
        this.rapidml_extensions = new ArrayList<>();
    }

    public rapidml_Extensible(
        ArrayList<rapidml_Extension> rapidml_extensions    ) {
        this.rapidml_extensions = rapidml_extensions;
    }


    public List<rapidml_Extension> getRapidml_extensions() {
        return rapidml_extensions;
    }

    public void addRapidml_extension(Rapidml_extension rapidml_extension) {
        this.rapidml_extensions.add(rapidml_extension);
    }

}