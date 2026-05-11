





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Tournament extends DescribedEntity {

    private String tournamentEnd;
    private int maxPlayers;
    private int defaultBuyIn;
    private int tournamentInvitationClosure;
    private int tournamentAnnouncementLead;
    private String tournamentStart;
    private String tournamentInvitationContact;
    private int minPlayers;





    private pokerleague_PrizeMoneyRuleSet pokerleague_prizemoneyruleset;




    private pokerleague_Competition pokerleague_competition;




    private pokerleague_Game pokerleague_game;




    private pokerleague_Competition pokerleague_competition;




    private List<pokerleague_Game> pokerleague_games;




    private List<pokerleague_Invitation> pokerleague_invitations;




    private pokerleague_Invitation pokerleague_invitation;


    public pokerleague_Tournament(
        String tournamentEnd,        int maxPlayers,        int defaultBuyIn,        int tournamentInvitationClosure,        int tournamentAnnouncementLead,        String tournamentStart,        String tournamentInvitationContact,        int minPlayers    ) {
        super(
        );
        this.tournamentEnd = tournamentEnd;
        this.maxPlayers = maxPlayers;
        this.defaultBuyIn = defaultBuyIn;
        this.tournamentInvitationClosure = tournamentInvitationClosure;
        this.tournamentAnnouncementLead = tournamentAnnouncementLead;
        this.tournamentStart = tournamentStart;
        this.tournamentInvitationContact = tournamentInvitationContact;
        this.minPlayers = minPlayers;
        this.pokerleague_games = new ArrayList<>();
        this.pokerleague_invitations = new ArrayList<>();
    }

    public pokerleague_Tournament(
        String tournamentEnd,        int maxPlayers,        int defaultBuyIn,        int tournamentInvitationClosure,        int tournamentAnnouncementLead,        String tournamentStart,        String tournamentInvitationContact,        int minPlayers        ArrayList<pokerleague_Game> pokerleague_games,        ArrayList<pokerleague_Invitation> pokerleague_invitations    ) {
        this.tournamentEnd = tournamentEnd;
        this.maxPlayers = maxPlayers;
        this.defaultBuyIn = defaultBuyIn;
        this.tournamentInvitationClosure = tournamentInvitationClosure;
        this.tournamentAnnouncementLead = tournamentAnnouncementLead;
        this.tournamentStart = tournamentStart;
        this.tournamentInvitationContact = tournamentInvitationContact;
        this.minPlayers = minPlayers;
        this.pokerleague_games = pokerleague_games;
        this.pokerleague_invitations = pokerleague_invitations;
    }

    public String getTournamentend() {
        return tournamentEnd;
    }

    public void setTournamentend(String tournamentEnd) {
        this.tournamentEnd = tournamentEnd;
    }
    public int getMaxplayers() {
        return maxPlayers;
    }

    public void setMaxplayers(int maxPlayers) {
        this.maxPlayers = maxPlayers;
    }
    public int getDefaultbuyin() {
        return defaultBuyIn;
    }

    public void setDefaultbuyin(int defaultBuyIn) {
        this.defaultBuyIn = defaultBuyIn;
    }
    public int getTournamentinvitationclosure() {
        return tournamentInvitationClosure;
    }

    public void setTournamentinvitationclosure(int tournamentInvitationClosure) {
        this.tournamentInvitationClosure = tournamentInvitationClosure;
    }
    public int getTournamentannouncementlead() {
        return tournamentAnnouncementLead;
    }

    public void setTournamentannouncementlead(int tournamentAnnouncementLead) {
        this.tournamentAnnouncementLead = tournamentAnnouncementLead;
    }
    public String getTournamentstart() {
        return tournamentStart;
    }

    public void setTournamentstart(String tournamentStart) {
        this.tournamentStart = tournamentStart;
    }
    public String getTournamentinvitationcontact() {
        return tournamentInvitationContact;
    }

    public void setTournamentinvitationcontact(String tournamentInvitationContact) {
        this.tournamentInvitationContact = tournamentInvitationContact;
    }
    public int getMinplayers() {
        return minPlayers;
    }

    public void setMinplayers(int minPlayers) {
        this.minPlayers = minPlayers;
    }

    public pokerleague_PrizeMoneyRuleSet getPokerleague_prizemoneyruleset() {
        return pokerleague_prizemoneyruleset;
    }

    public void setPokerleague_prizemoneyruleset(pokerleague_PrizeMoneyRuleSet pokerleague_prizemoneyruleset) {
        this.pokerleague_prizemoneyruleset = pokerleague_prizemoneyruleset;
    }
    public pokerleague_Competition getPokerleague_competition() {
        return pokerleague_competition;
    }

    public void setPokerleague_competition(pokerleague_Competition pokerleague_competition) {
        this.pokerleague_competition = pokerleague_competition;
    }
    public pokerleague_Game getPokerleague_game() {
        return pokerleague_game;
    }

    public void setPokerleague_game(pokerleague_Game pokerleague_game) {
        this.pokerleague_game = pokerleague_game;
    }
    public pokerleague_Competition getPokerleague_competition() {
        return pokerleague_competition;
    }

    public void setPokerleague_competition(pokerleague_Competition pokerleague_competition) {
        this.pokerleague_competition = pokerleague_competition;
    }
    public List<pokerleague_Game> getPokerleague_games() {
        return pokerleague_games;
    }

    public void addPokerleague_game(Pokerleague_game pokerleague_game) {
        this.pokerleague_games.add(pokerleague_game);
    }
    public List<pokerleague_Invitation> getPokerleague_invitations() {
        return pokerleague_invitations;
    }

    public void addPokerleague_invitation(Pokerleague_invitation pokerleague_invitation) {
        this.pokerleague_invitations.add(pokerleague_invitation);
    }
    public pokerleague_Invitation getPokerleague_invitation() {
        return pokerleague_invitation;
    }

    public void setPokerleague_invitation(pokerleague_Invitation pokerleague_invitation) {
        this.pokerleague_invitation = pokerleague_invitation;
    }

}