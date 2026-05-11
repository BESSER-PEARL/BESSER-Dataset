





import java.util.List;
import java.util.ArrayList;

public class klang_CollisionEvent extends ActorEvent {






    private klang_SpriteActor klang_spriteactor;


    public klang_CollisionEvent(
    ) {
        super(
        );
    }



    public klang_SpriteActor getKlang_spriteactor() {
        return klang_spriteactor;
    }

    public void setKlang_spriteactor(klang_SpriteActor klang_spriteactor) {
        this.klang_spriteactor = klang_spriteactor;
    }

}