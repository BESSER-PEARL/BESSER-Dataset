





import java.util.List;
import java.util.ArrayList;

public class baseCST_RootCS extends ModelElementCS {






    private List<baseCST_LibraryCS> basecst_librarycss;




    private List<baseCST_ImportCS> basecst_importcss;


    public baseCST_RootCS(
    ) {
        super(
        );
        this.basecst_librarycss = new ArrayList<>();
        this.basecst_importcss = new ArrayList<>();
    }

    public baseCST_RootCS(
        ArrayList<baseCST_LibraryCS> basecst_librarycss,        ArrayList<baseCST_ImportCS> basecst_importcss    ) {
        this.basecst_librarycss = basecst_librarycss;
        this.basecst_importcss = basecst_importcss;
    }


    public List<baseCST_LibraryCS> getBasecst_librarycss() {
        return basecst_librarycss;
    }

    public void addBasecst_librarycs(Basecst_librarycs basecst_librarycs) {
        this.basecst_librarycss.add(basecst_librarycs);
    }
    public List<baseCST_ImportCS> getBasecst_importcss() {
        return basecst_importcss;
    }

    public void addBasecst_importcs(Basecst_importcs basecst_importcs) {
        this.basecst_importcss.add(basecst_importcs);
    }

}