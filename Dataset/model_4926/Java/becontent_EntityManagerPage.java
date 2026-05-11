





import java.util.List;
import java.util.ArrayList;

public class becontent_EntityManagerPage extends BeContentElement {

    private String skin;
    private String fileName;





    private List<becontent_Validation> becontent_validations;


    public becontent_EntityManagerPage(
        String skin,        String fileName    ) {
        super(
        );
        this.skin = skin;
        this.fileName = fileName;
        this.becontent_validations = new ArrayList<>();
    }

    public becontent_EntityManagerPage(
        String skin,        String fileName        ArrayList<becontent_Validation> becontent_validations    ) {
        this.skin = skin;
        this.fileName = fileName;
        this.becontent_validations = becontent_validations;
    }

    public String getSkin() {
        return skin;
    }

    public void setSkin(String skin) {
        this.skin = skin;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public List<becontent_Validation> getBecontent_validations() {
        return becontent_validations;
    }

    public void addBecontent_validation(Becontent_validation becontent_validation) {
        this.becontent_validations.add(becontent_validation);
    }

}