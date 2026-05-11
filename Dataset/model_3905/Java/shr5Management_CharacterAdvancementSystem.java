





import java.util.List;
import java.util.ArrayList;

public class shr5Management_CharacterAdvancementSystem extends Beschreibbar {






    private List<shr5Management_Advancement> shr5management_advancements;




    private shr5Management_CharacterGeneratorSystem shr5management_charactergeneratorsystem;


    public shr5Management_CharacterAdvancementSystem(
    ) {
        super(
        );
        this.shr5management_advancements = new ArrayList<>();
    }

    public shr5Management_CharacterAdvancementSystem(
        ArrayList<shr5Management_Advancement> shr5management_advancements    ) {
        this.shr5management_advancements = shr5management_advancements;
    }


    public List<shr5Management_Advancement> getShr5management_advancements() {
        return shr5management_advancements;
    }

    public void addShr5management_advancement(Shr5management_advancement shr5management_advancement) {
        this.shr5management_advancements.add(shr5management_advancement);
    }
    public shr5Management_CharacterGeneratorSystem getShr5management_charactergeneratorsystem() {
        return shr5management_charactergeneratorsystem;
    }

    public void setShr5management_charactergeneratorsystem(shr5Management_CharacterGeneratorSystem shr5management_charactergeneratorsystem) {
        this.shr5management_charactergeneratorsystem = shr5management_charactergeneratorsystem;
    }

}