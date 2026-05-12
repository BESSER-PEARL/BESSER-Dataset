





import java.util.List;
import java.util.ArrayList;

public class LoginView  {

    private None user;





    private GameLauncher gamelauncher;


    public LoginView(
        None user    ) {
        this.user = user;
    }


    public None getUser() {
        return user;
    }

    public void setUser(None user) {
        this.user = user;
    }

    public GameLauncher getGamelauncher() {
        return gamelauncher;
    }

    public void setGamelauncher(GameLauncher gamelauncher) {
        this.gamelauncher = gamelauncher;
    }

}