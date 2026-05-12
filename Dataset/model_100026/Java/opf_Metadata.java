





import java.util.List;
import java.util.ArrayList;

public class opf_Metadata  {






    private List<opf_Title> opf_titles;




    private opf_Package opf_package;


    public opf_Metadata(
    ) {
        this.opf_titles = new ArrayList<>();
    }

    public opf_Metadata(
        ArrayList<opf_Title> opf_titles    ) {
        this.opf_titles = opf_titles;
    }


    public List<opf_Title> getOpf_titles() {
        return opf_titles;
    }

    public void addOpf_title(Opf_title opf_title) {
        this.opf_titles.add(opf_title);
    }
    public opf_Package getOpf_package() {
        return opf_package;
    }

    public void setOpf_package(opf_Package opf_package) {
        this.opf_package = opf_package;
    }

}