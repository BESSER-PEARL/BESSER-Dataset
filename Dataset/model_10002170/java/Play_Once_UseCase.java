





import java.util.List;
import java.util.ArrayList;

public class Play_Once_UseCase  {






    private Play_for_Me_UseCase play_for_me_usecase;


    public Play_Once_UseCase(
    ) {
    }



    public Play_for_Me_UseCase getPlay_for_me_usecase() {
        return play_for_me_usecase;
    }

    public void setPlay_for_me_usecase(Play_for_Me_UseCase play_for_me_usecase) {
        this.play_for_me_usecase = play_for_me_usecase;
    }

}