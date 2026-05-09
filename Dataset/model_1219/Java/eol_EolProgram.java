





import java.util.List;
import java.util.ArrayList;

public class eol_EolProgram extends EolLibraryModule {






    private List<eol_EolProgram> eol_eolprograms;


    public eol_EolProgram(
    ) {
        super(
        );
        this.eol_eolprograms = new ArrayList<>();
    }

    public eol_EolProgram(
        ArrayList<eol_EolProgram> eol_eolprograms    ) {
        this.eol_eolprograms = eol_eolprograms;
    }


    public List<eol_EolProgram> getEol_eolprograms() {
        return eol_eolprograms;
    }

    public void addEol_eolprogram(Eol_eolprogram eol_eolprogram) {
        this.eol_eolprograms.add(eol_eolprogram);
    }

}