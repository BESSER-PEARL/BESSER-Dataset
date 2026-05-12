





import java.util.List;
import java.util.ArrayList;

public class CommentServiceTest  {

    private String PLAYER_NAME;
    private String GAME_NAME;





    private services_CommentService_Interface services_commentservice_interface;


    public CommentServiceTest(
        String PLAYER_NAME,        String GAME_NAME    ) {
        this.PLAYER_NAME = PLAYER_NAME;
        this.GAME_NAME = GAME_NAME;
    }


    public String getPlayer_name() {
        return PLAYER_NAME;
    }

    public void setPlayer_name(String PLAYER_NAME) {
        this.PLAYER_NAME = PLAYER_NAME;
    }
    public String getGame_name() {
        return GAME_NAME;
    }

    public void setGame_name(String GAME_NAME) {
        this.GAME_NAME = GAME_NAME;
    }

    public services_CommentService_Interface getServices_commentservice_interface() {
        return services_commentservice_interface;
    }

    public void setServices_commentservice_interface(services_CommentService_Interface services_commentservice_interface) {
        this.services_commentservice_interface = services_commentservice_interface;
    }

}