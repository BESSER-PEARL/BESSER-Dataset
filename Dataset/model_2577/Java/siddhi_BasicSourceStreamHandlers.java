





import java.util.List;
import java.util.ArrayList;

public class siddhi_BasicSourceStreamHandlers  {






    private siddhi_StandardStatefulSource siddhi_standardstatefulsource;




    private siddhi_BasicSource siddhi_basicsource;




    private List<siddhi_BasicSourceStreamHandler> siddhi_basicsourcestreamhandlers;




    private siddhi_MainSource siddhi_mainsource;


    public siddhi_BasicSourceStreamHandlers(
    ) {
        this.siddhi_basicsourcestreamhandlers = new ArrayList<>();
    }

    public siddhi_BasicSourceStreamHandlers(
        ArrayList<siddhi_BasicSourceStreamHandler> siddhi_basicsourcestreamhandlers    ) {
        this.siddhi_basicsourcestreamhandlers = siddhi_basicsourcestreamhandlers;
    }


    public siddhi_StandardStatefulSource getSiddhi_standardstatefulsource() {
        return siddhi_standardstatefulsource;
    }

    public void setSiddhi_standardstatefulsource(siddhi_StandardStatefulSource siddhi_standardstatefulsource) {
        this.siddhi_standardstatefulsource = siddhi_standardstatefulsource;
    }
    public siddhi_BasicSource getSiddhi_basicsource() {
        return siddhi_basicsource;
    }

    public void setSiddhi_basicsource(siddhi_BasicSource siddhi_basicsource) {
        this.siddhi_basicsource = siddhi_basicsource;
    }
    public List<siddhi_BasicSourceStreamHandler> getSiddhi_basicsourcestreamhandlers() {
        return siddhi_basicsourcestreamhandlers;
    }

    public void addSiddhi_basicsourcestreamhandler(Siddhi_basicsourcestreamhandler siddhi_basicsourcestreamhandler) {
        this.siddhi_basicsourcestreamhandlers.add(siddhi_basicsourcestreamhandler);
    }
    public siddhi_MainSource getSiddhi_mainsource() {
        return siddhi_mainsource;
    }

    public void setSiddhi_mainsource(siddhi_MainSource siddhi_mainsource) {
        this.siddhi_mainsource = siddhi_mainsource;
    }

}