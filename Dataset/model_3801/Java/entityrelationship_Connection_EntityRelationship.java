





import java.util.List;
import java.util.ArrayList;

public class entityrelationship_Connection_EntityRelationship  {

    private String minimum_cardinality;
    private String role;
    private String maximum_cardinality;





    private entityrelationship_Connection_E_R_Restriction entityrelationship_connection_e_r_restriction;




    private entityrelationship_Connection_E_R_Restriction entityrelationship_connection_e_r_restriction;




    private entityrelationship_Connection_ConnectionEntityRelationship2Attribute entityrelationship_connection_connectionentityrelationship2attribute;


    public entityrelationship_Connection_EntityRelationship(
        String minimum_cardinality,        String role,        String maximum_cardinality    ) {
        this.minimum_cardinality = minimum_cardinality;
        this.role = role;
        this.maximum_cardinality = maximum_cardinality;
    }


    public String getMinimum_cardinality() {
        return minimum_cardinality;
    }

    public void setMinimum_cardinality(String minimum_cardinality) {
        this.minimum_cardinality = minimum_cardinality;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getMaximum_cardinality() {
        return maximum_cardinality;
    }

    public void setMaximum_cardinality(String maximum_cardinality) {
        this.maximum_cardinality = maximum_cardinality;
    }

    public entityrelationship_Connection_E_R_Restriction getEntityrelationship_connection_e_r_restriction() {
        return entityrelationship_connection_e_r_restriction;
    }

    public void setEntityrelationship_connection_e_r_restriction(entityrelationship_Connection_E_R_Restriction entityrelationship_connection_e_r_restriction) {
        this.entityrelationship_connection_e_r_restriction = entityrelationship_connection_e_r_restriction;
    }
    public entityrelationship_Connection_E_R_Restriction getEntityrelationship_connection_e_r_restriction() {
        return entityrelationship_connection_e_r_restriction;
    }

    public void setEntityrelationship_connection_e_r_restriction(entityrelationship_Connection_E_R_Restriction entityrelationship_connection_e_r_restriction) {
        this.entityrelationship_connection_e_r_restriction = entityrelationship_connection_e_r_restriction;
    }
    public entityrelationship_Connection_ConnectionEntityRelationship2Attribute getEntityrelationship_connection_connectionentityrelationship2attribute() {
        return entityrelationship_connection_connectionentityrelationship2attribute;
    }

    public void setEntityrelationship_connection_connectionentityrelationship2attribute(entityrelationship_Connection_ConnectionEntityRelationship2Attribute entityrelationship_connection_connectionentityrelationship2attribute) {
        this.entityrelationship_connection_connectionentityrelationship2attribute = entityrelationship_connection_connectionentityrelationship2attribute;
    }

}