// This file is auto-generated. Do not edit this file manually.
//
// Disable formatting for this file to avoid linting errors.
// tslint:disable
// @ts-nocheck
/* eslint-disable */


import { GPT35 } from '../client';
import { FnTestOutputAdapter } from '../function';
import { schema } from '../json_schema';
import { Deserializer } from '@boundaryml/baml-core/deserializer/deserializer';


const prompt_template = `\
Question: What is the capital of France?

Return in this format:
{
  "REASONING": string,
  "ANSWER": string
}

JSON:\
`;

const deserializer = new Deserializer<string>(schema, {
  $ref: '#/definitions/FnTestOutputAdapter_output'
});

FnTestOutputAdapter.registerImpl('v1', async (
  arg: string
): Promise<string> => {
  
    const result = await GPT35.run_prompt_template(
      prompt_template,
      [],
      {
      }
    );

    return deserializer.coerce(result.generated);
  }
);

