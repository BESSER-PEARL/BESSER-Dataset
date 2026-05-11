





import java.util.List;
import java.util.ArrayList;

public class delphi_procedureDeclSection extends declSection {

    private String port;





    private delphi_block delphi_block;




    private delphi_directive delphi_directive;


    public delphi_procedureDeclSection(
        String port    ) {
        super(
        );
        this.port = port;
    }


    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }

    public delphi_block getDelphi_block() {
        return delphi_block;
    }

    public void setDelphi_block(delphi_block delphi_block) {
        this.delphi_block = delphi_block;
    }
    public delphi_directive getDelphi_directive() {
        return delphi_directive;
    }

    public void setDelphi_directive(delphi_directive delphi_directive) {
        this.delphi_directive = delphi_directive;
    }

}