





import java.util.List;
import java.util.ArrayList;

public class aDSL_Block  {

    private boolean ispar;





    private List<aDSL_Statement> adsl_statements;




    private aDSL_For2Statement adsl_for2statement;




    private aDSL_AsyncStat adsl_asyncstat;




    private aDSL_FinishStat adsl_finishstat;




    private aDSL_AtStat adsl_atstat;




    private aDSL_ForStat adsl_forstat;




    private aDSL_IfStat adsl_ifstat;




    private aDSL_IfStat adsl_ifstat;


    public aDSL_Block(
        boolean ispar    ) {
        this.ispar = ispar;
        this.adsl_statements = new ArrayList<>();
    }

    public aDSL_Block(
        boolean ispar        ArrayList<aDSL_Statement> adsl_statements    ) {
        this.ispar = ispar;
        this.adsl_statements = adsl_statements;
    }

    public boolean getIspar() {
        return ispar;
    }

    public void setIspar(boolean ispar) {
        this.ispar = ispar;
    }

    public List<aDSL_Statement> getAdsl_statements() {
        return adsl_statements;
    }

    public void addAdsl_statement(Adsl_statement adsl_statement) {
        this.adsl_statements.add(adsl_statement);
    }
    public aDSL_For2Statement getAdsl_for2statement() {
        return adsl_for2statement;
    }

    public void setAdsl_for2statement(aDSL_For2Statement adsl_for2statement) {
        this.adsl_for2statement = adsl_for2statement;
    }
    public aDSL_AsyncStat getAdsl_asyncstat() {
        return adsl_asyncstat;
    }

    public void setAdsl_asyncstat(aDSL_AsyncStat adsl_asyncstat) {
        this.adsl_asyncstat = adsl_asyncstat;
    }
    public aDSL_FinishStat getAdsl_finishstat() {
        return adsl_finishstat;
    }

    public void setAdsl_finishstat(aDSL_FinishStat adsl_finishstat) {
        this.adsl_finishstat = adsl_finishstat;
    }
    public aDSL_AtStat getAdsl_atstat() {
        return adsl_atstat;
    }

    public void setAdsl_atstat(aDSL_AtStat adsl_atstat) {
        this.adsl_atstat = adsl_atstat;
    }
    public aDSL_ForStat getAdsl_forstat() {
        return adsl_forstat;
    }

    public void setAdsl_forstat(aDSL_ForStat adsl_forstat) {
        this.adsl_forstat = adsl_forstat;
    }
    public aDSL_IfStat getAdsl_ifstat() {
        return adsl_ifstat;
    }

    public void setAdsl_ifstat(aDSL_IfStat adsl_ifstat) {
        this.adsl_ifstat = adsl_ifstat;
    }
    public aDSL_IfStat getAdsl_ifstat() {
        return adsl_ifstat;
    }

    public void setAdsl_ifstat(aDSL_IfStat adsl_ifstat) {
        this.adsl_ifstat = adsl_ifstat;
    }

}