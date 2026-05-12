





import java.util.List;
import java.util.ArrayList;

public class ScoreServiceTest  {

    private String GAME_NAME;





    private services_ScoreService_Interface services_scoreservice_interface;


    public ScoreServiceTest(
        String GAME_NAME    ) {
        this.GAME_NAME = GAME_NAME;
    }


    public String getGame_name() {
        return GAME_NAME;
    }

    public void setGame_name(String GAME_NAME) {
        this.GAME_NAME = GAME_NAME;
    }

    public services_ScoreService_Interface getServices_scoreservice_interface() {
        return services_scoreservice_interface;
    }

    public void setServices_scoreservice_interface(services_ScoreService_Interface services_scoreservice_interface) {
        this.services_scoreservice_interface = services_scoreservice_interface;
    }

}