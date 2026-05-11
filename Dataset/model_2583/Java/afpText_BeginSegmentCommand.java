





import java.util.List;
import java.util.ArrayList;

public class afpText_BeginSegmentCommand extends triplet {

    private String PSNAME;
    private String SEGL;
    private String NAME;
    private String LENGTH;
    private String FLAG2;
    private String FLAG1;



    public afpText_BeginSegmentCommand(
        String PSNAME,        String SEGL,        String NAME,        String LENGTH,        String FLAG2,        String FLAG1    ) {
        super(
        );
        this.PSNAME = PSNAME;
        this.SEGL = SEGL;
        this.NAME = NAME;
        this.LENGTH = LENGTH;
        this.FLAG2 = FLAG2;
        this.FLAG1 = FLAG1;
    }


    public String getPsname() {
        return PSNAME;
    }

    public void setPsname(String PSNAME) {
        this.PSNAME = PSNAME;
    }
    public String getSegl() {
        return SEGL;
    }

    public void setSegl(String SEGL) {
        this.SEGL = SEGL;
    }
    public String getName() {
        return NAME;
    }

    public void setName(String NAME) {
        this.NAME = NAME;
    }
    public String getLength() {
        return LENGTH;
    }

    public void setLength(String LENGTH) {
        this.LENGTH = LENGTH;
    }
    public String getFlag2() {
        return FLAG2;
    }

    public void setFlag2(String FLAG2) {
        this.FLAG2 = FLAG2;
    }
    public String getFlag1() {
        return FLAG1;
    }

    public void setFlag1(String FLAG1) {
        this.FLAG1 = FLAG1;
    }


}