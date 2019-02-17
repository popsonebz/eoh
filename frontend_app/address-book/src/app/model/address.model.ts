export class Address {
    constructor(
      public first_name: string,
      public last_name: string,
      public email: string,
      public phone_number?: string,
      public id?: number,
      public created_a?: Date,
      public modified_at?: Date,
      
    ) { }
  }