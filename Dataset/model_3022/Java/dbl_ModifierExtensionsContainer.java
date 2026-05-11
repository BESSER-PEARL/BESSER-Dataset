





import java.util.List;
import java.util.ArrayList;

public class dbl_ModifierExtensionsContainer  {






    private List<dbl_Extension> dbl_extensions;


    public dbl_ModifierExtensionsContainer(
    ) {
        this.dbl_extensions = new ArrayList<>();
    }

    public dbl_ModifierExtensionsContainer(
        ArrayList<dbl_Extension> dbl_extensions    ) {
        this.dbl_extensions = dbl_extensions;
    }


    public List<dbl_Extension> getDbl_extensions() {
        return dbl_extensions;
    }

    public void addDbl_extension(Dbl_extension dbl_extension) {
        this.dbl_extensions.add(dbl_extension);
    }

}