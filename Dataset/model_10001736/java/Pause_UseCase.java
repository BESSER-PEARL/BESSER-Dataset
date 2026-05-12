





import java.util.List;
import java.util.ArrayList;

public class Pause_UseCase  {






    private Play_UseCase play_usecase;


    public Pause_UseCase(
    ) {
    }



    public Play_UseCase getPlay_usecase() {
        return play_usecase;
    }

    public void setPlay_usecase(Play_UseCase play_usecase) {
        this.play_usecase = play_usecase;
    }

}