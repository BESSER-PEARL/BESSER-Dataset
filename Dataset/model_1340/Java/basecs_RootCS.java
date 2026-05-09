





import java.util.List;
import java.util.ArrayList;

public class basecs_RootCS extends ModelElementCS {






    private List<basecs_LibraryCS> basecs_librarycss;




    private List<basecs_ImportCS> basecs_importcss;


    public basecs_RootCS(
    ) {
        super(
        );
        this.basecs_librarycss = new ArrayList<>();
        this.basecs_importcss = new ArrayList<>();
    }

    public basecs_RootCS(
        ArrayList<basecs_LibraryCS> basecs_librarycss,        ArrayList<basecs_ImportCS> basecs_importcss    ) {
        this.basecs_librarycss = basecs_librarycss;
        this.basecs_importcss = basecs_importcss;
    }


    public List<basecs_LibraryCS> getBasecs_librarycss() {
        return basecs_librarycss;
    }

    public void addBasecs_librarycs(Basecs_librarycs basecs_librarycs) {
        this.basecs_librarycss.add(basecs_librarycs);
    }
    public List<basecs_ImportCS> getBasecs_importcss() {
        return basecs_importcss;
    }

    public void addBasecs_importcs(Basecs_importcs basecs_importcs) {
        this.basecs_importcss.add(basecs_importcs);
    }

}