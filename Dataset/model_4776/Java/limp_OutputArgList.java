





import java.util.List;
import java.util.ArrayList;

public class limp_OutputArgList  {






    private limp_ExternalProcedure limp_externalprocedure;




    private List<limp_OutputArg> limp_outputargs;




    private limp_LocalProcedure limp_localprocedure;


    public limp_OutputArgList(
    ) {
        this.limp_outputargs = new ArrayList<>();
    }

    public limp_OutputArgList(
        ArrayList<limp_OutputArg> limp_outputargs    ) {
        this.limp_outputargs = limp_outputargs;
    }


    public limp_ExternalProcedure getLimp_externalprocedure() {
        return limp_externalprocedure;
    }

    public void setLimp_externalprocedure(limp_ExternalProcedure limp_externalprocedure) {
        this.limp_externalprocedure = limp_externalprocedure;
    }
    public List<limp_OutputArg> getLimp_outputargs() {
        return limp_outputargs;
    }

    public void addLimp_outputarg(Limp_outputarg limp_outputarg) {
        this.limp_outputargs.add(limp_outputarg);
    }
    public limp_LocalProcedure getLimp_localprocedure() {
        return limp_localprocedure;
    }

    public void setLimp_localprocedure(limp_LocalProcedure limp_localprocedure) {
        this.limp_localprocedure = limp_localprocedure;
    }

}