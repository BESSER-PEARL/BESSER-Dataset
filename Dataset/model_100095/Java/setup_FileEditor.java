





import java.util.List;
import java.util.ArrayList;

public class setup_FileEditor  {

    private String iD;





    private setup_FileAssociationTask setup_fileassociationtask;




    private setup_FileMapping setup_filemapping;


    public setup_FileEditor(
        String iD    ) {
        this.iD = iD;
    }


    public String getId() {
        return iD;
    }

    public void setId(String iD) {
        this.iD = iD;
    }

    public setup_FileAssociationTask getSetup_fileassociationtask() {
        return setup_fileassociationtask;
    }

    public void setSetup_fileassociationtask(setup_FileAssociationTask setup_fileassociationtask) {
        this.setup_fileassociationtask = setup_fileassociationtask;
    }
    public setup_FileMapping getSetup_filemapping() {
        return setup_filemapping;
    }

    public void setSetup_filemapping(setup_FileMapping setup_filemapping) {
        this.setup_filemapping = setup_filemapping;
    }

}