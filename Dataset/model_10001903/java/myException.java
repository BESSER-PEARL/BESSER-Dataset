





import java.util.List;
import java.util.ArrayList;

public class myException  {






    private auftrag auftrag;




    private lager lager;




    private backofen backofen;


    public myException(
    ) {
    }



    public auftrag getAuftrag() {
        return auftrag;
    }

    public void setAuftrag(auftrag auftrag) {
        this.auftrag = auftrag;
    }
    public lager getLager() {
        return lager;
    }

    public void setLager(lager lager) {
        this.lager = lager;
    }
    public backofen getBackofen() {
        return backofen;
    }

    public void setBackofen(backofen backofen) {
        this.backofen = backofen;
    }

}