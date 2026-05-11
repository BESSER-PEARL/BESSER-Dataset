





import java.util.List;
import java.util.ArrayList;

public class limp_InputArgList  {






    private limp_ExternalFunction limp_externalfunction;




    private limp_LocalFunction limp_localfunction;




    private limp_LocalProcedure limp_localprocedure;




    private limp_ExternalProcedure limp_externalprocedure;


    public limp_InputArgList(
    ) {
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
    public limp_LocalProcedure getLimp_localprocedure() {
        return limp_localprocedure;
    }

    public void setLimp_localprocedure(limp_LocalProcedure limp_localprocedure) {
        this.limp_localprocedure = limp_localprocedure;
    }
    public limp_ExternalProcedure getLimp_externalprocedure() {
        return limp_externalprocedure;
    }

    public void setLimp_externalprocedure(limp_ExternalProcedure limp_externalprocedure) {
        this.limp_externalprocedure = limp_externalprocedure;
    }

}