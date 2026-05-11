





import java.util.List;
import java.util.ArrayList;

public class iec61131_pous_String_Type_Declaration extends Type_Declaration {






    private Assignment_Symbol assignment_symbol;




    private Character_String character_string;




    private Unsigned_Integer unsigned_integer;


    public iec61131_pous_String_Type_Declaration(
    ) {
        super(
        );
    }



    public Assignment_Symbol getAssignment_symbol() {
        return assignment_symbol;
    }

    public void setAssignment_symbol(Assignment_Symbol assignment_symbol) {
        this.assignment_symbol = assignment_symbol;
    }
    public Character_String getCharacter_string() {
        return character_string;
    }

    public void setCharacter_string(Character_String character_string) {
        this.character_string = character_string;
    }
    public Unsigned_Integer getUnsigned_integer() {
        return unsigned_integer;
    }

    public void setUnsigned_integer(Unsigned_Integer unsigned_integer) {
        this.unsigned_integer = unsigned_integer;
    }

}