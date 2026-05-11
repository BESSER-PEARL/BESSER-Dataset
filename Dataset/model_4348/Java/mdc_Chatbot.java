





import java.util.List;
import java.util.ArrayList;

public class mdc_Chatbot  {

    private String tokenNluService;
    private String nluService;
    private String token;
    private String name;
    private String mensageiro;





    private mdc_StationaryState mdc_stationarystate;


    public mdc_Chatbot(
        String tokenNluService,        String nluService,        String token,        String name,        String mensageiro    ) {
        this.tokenNluService = tokenNluService;
        this.nluService = nluService;
        this.token = token;
        this.name = name;
        this.mensageiro = mensageiro;
    }


    public String getTokennluservice() {
        return tokenNluService;
    }

    public void setTokennluservice(String tokenNluService) {
        this.tokenNluService = tokenNluService;
    }
    public String getNluservice() {
        return nluService;
    }

    public void setNluservice(String nluService) {
        this.nluService = nluService;
    }
    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMensageiro() {
        return mensageiro;
    }

    public void setMensageiro(String mensageiro) {
        this.mensageiro = mensageiro;
    }

    public mdc_StationaryState getMdc_stationarystate() {
        return mdc_stationarystate;
    }

    public void setMdc_stationarystate(mdc_StationaryState mdc_stationarystate) {
        this.mdc_stationarystate = mdc_stationarystate;
    }

}