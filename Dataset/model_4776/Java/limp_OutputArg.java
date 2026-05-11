





import java.util.List;
import java.util.ArrayList;

public class limp_OutputArg extends VariableRef {






    private limp_ExternalFunction limp_externalfunction;




    private limp_LocalFunction limp_localfunction;


    public limp_OutputArg(
    ) {
        super(
        );
    }



    public limp_ExternalFunction getLimp_externalfunction() {
        return limp_externalfunction;
    }

    public void setLimp_externalfunction(limp_ExternalFunction limp_externalfunction) {
        this.limp_externalfunction = limp_externalfunction;
    }
    public limp_LocalFunction getLimp_localfunction() {
        return limp_localfunction;
    }

    public void setLimp_localfunction(limp_LocalFunction limp_localfunction) {
        this.limp_localfunction = limp_localfunction;
    }

}