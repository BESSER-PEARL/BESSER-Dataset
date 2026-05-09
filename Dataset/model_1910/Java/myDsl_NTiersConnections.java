





import java.util.List;
import java.util.ArrayList;

public class myDsl_NTiersConnections  {

    private String ntierconnection;
    private String name;



    public myDsl_NTiersConnections(
        String ntierconnection,        String name    ) {
        this.ntierconnection = ntierconnection;
        this.name = name;
    }


    public String getNtierconnection() {
        return ntierconnection;
    }

    public void setNtierconnection(String ntierconnection) {
        this.ntierconnection = ntierconnection;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}